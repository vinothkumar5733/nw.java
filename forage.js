const fs = require("fs");
const path = require("path");
const sqlite3 = require("sqlite3").verbose();

const BASE_DIR = __dirname;
const DATA_DIR = path.join(BASE_DIR, "data");
const DATABASE_PATH = path.join(BASE_DIR, "shipment_database.db");

const files = {
	simple: path.join(DATA_DIR, "shipping_data_0.csv"),
	units: path.join(DATA_DIR, "shipping_data_1.csv"),
	locations: path.join(DATA_DIR, "shipping_data_2.csv")
};

function readCsv(file) {
	const lines = fs.readFileSync(file, "utf8").trim().split(/\r?\n/);
	if (!lines.length || !lines[0]) return [];
	const headers = lines.shift().split(",");
	return lines.map(line => {
		const values = line.split(",");
		return Object.fromEntries(headers.map((header, i) => [header, (values[i] || "").trim()]));
	});
}

function run(db, sql, params = []) {
	return new Promise((resolve, reject) => {
		db.run(sql, params, function (error) {
			if (error) reject(error);
			else resolve(this);
		});
	});
}

function all(db, sql, params = []) {
	return new Promise((resolve, reject) => {
		db.all(sql, params, (error, rows) => error ? reject(error) : resolve(rows));
	});
}

async function getProductId(db, cache, name) {
	if (cache.has(name)) return cache.get(name);
	const rows = await all(db, "SELECT id FROM product WHERE name = ?", [name]);
	let id;
	if (rows.length) id = rows[0].id;
	else id = (await run(db, "INSERT INTO product (name) VALUES (?)", [name])).lastID;
	cache.set(name, id);
	return id;
}

async function insertShipments(db, cache, shipments) {
	let count = 0;
	for (const shipment of shipments) {
		const productId = await getProductId(db, cache, shipment.product);
		await run(db,
			"INSERT INTO shipment (product_id, quantity, origin, destination) VALUES (?, ?, ?, ?)",
			[productId, shipment.quantity, shipment.origin, shipment.destination]);
		count++;
	}
	return count;
}

async function main() {
	const db = new sqlite3.Database(DATABASE_PATH);
	const cache = new Map();
	try {
		await run(db, "BEGIN TRANSACTION");
		const simple = readCsv(files.simple).map(row => ({
			product: row.product,
			quantity: Number(row.product_quantity),
			origin: row.origin_warehouse,
			destination: row.destination_store
		}));
		const locations = Object.fromEntries(readCsv(files.locations).map(row => [
			row.shipment_identifier,
			{ origin: row.origin_warehouse, destination: row.destination_store }
		]));
		const grouped = new Map();
		for (const row of readCsv(files.units)) {
			const key = `${row.shipment_identifier}\u0000${row.product}`;
			const item = grouped.get(key) || { product: row.product, quantity: 0,
				...locations[row.shipment_identifier] };
			item.quantity++;
			grouped.set(key, item);
		}
		const simpleCount = await insertShipments(db, cache, simple);
		const groupedCount = await insertShipments(db, cache, grouped.values());
		await run(db, "COMMIT");
		console.log(`Inserted ${simpleCount} shipments from shipping_data_0.csv`);
		console.log(`Inserted ${groupedCount} shipments from shipping_data_1.csv (joined with shipping_data_2.csv)`);
		console.log(`Total distinct products: ${cache.size}`);
	} catch (error) {
		await run(db, "ROLLBACK").catch(() => {});
		throw error;
	} finally {
		db.close();
	}
}

if (require.main === module) main().catch(error => {
	console.error(error);
	process.exitCode = 1;
});
