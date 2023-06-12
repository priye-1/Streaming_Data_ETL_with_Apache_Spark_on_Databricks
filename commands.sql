-- create an admin user
use admin
db.createUser(
    {
    user: "user1",
    pwd: "pass!1dfggh456f",
    roles: [
        { role: "userAdminAnyDatabase", db: "admin" },
        { role: "dbAdminAnyDatabase", db: "admin" },
        { role: "readWriteAnyDatabase", db: "admin" }
        ]
    }
)

-- create database 
use stocks_DB

-- create collection
db.createCollection("stocks")

-- insert document into collection
db.stocks.insertOne({
    car: "ford",
    price: 15500,
    body:  "crossover",
    mileage: 68,
    engV: 2.5,
    engType: "Gas",
    registration: "yes",
    year: 2010,
    model: "kuga",
    drive: "full",
})

-- print from table
db.COLLECTION_NAME.find()

