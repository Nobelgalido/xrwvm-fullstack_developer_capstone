const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 3050;

app.use(cors());
app.use(express.urlencoded({ extended: false }));

const Cars = require('./inventory');

// Read car records from JSON file
const cars_data = JSON.parse(fs.readFileSync("data/car_records.json", 'utf8'));

// Connect to MongoDB
mongoose.connect("mongodb://mongo_db:27017/", { dbName: 'dealershipsDB' });

// Populate database with car data
try {
  Cars.deleteMany({}).then(() => {
    Cars.insertMany(cars_data.cars);
  });
} catch (error) {
  console.error('Error initializing data:', error);
}

// Root endpoint
app.get('/', async (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// Get all cars by dealer ID
app.get('/cars/:id', async (req, res) => {
  try {
    const documents = await Cars.find({ dealer_id: req.params.id });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Get cars by dealer ID and make
app.get('/carsbymake/:id/:make', async (req, res) => {
  try {
    const documents = await Cars.find({ 
      dealer_id: req.params.id, 
      make: req.params.make 
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Get cars by dealer ID and model
app.get('/carsbymodel/:id/:model', async (req, res) => {
  try {
    const documents = await Cars.find({ 
      dealer_id: req.params.id, 
      model: req.params.model 
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Get cars by dealer ID and max mileage
app.get('/carsbymaxmileage/:id/:mileage', async (req, res) => {
  try {
    const mileage = parseInt(req.params.mileage);
    let query = { dealer_id: req.params.id };

    if (mileage <= 50000) {
      query.mileage = { $lte: 50000 };
    } else if (mileage > 50000 && mileage <= 100000) {
      query.mileage = { $gt: 50000, $lte: 100000 };
    } else if (mileage > 100000 && mileage <= 150000) {
      query.mileage = { $gt: 100000, $lte: 150000 };
    } else if (mileage > 150000 && mileage <= 200000) {
      query.mileage = { $gt: 150000, $lte: 200000 };
    } else {
      query.mileage = { $gt: 200000 };
    }

    const documents = await Cars.find(query);
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Get cars by dealer ID and price range
app.get('/carsbyprice/:id/:price', async (req, res) => {
  try {
    const price = parseInt(req.params.price);
    let query = { dealer_id: req.params.id };

    if (price <= 20000) {
      query.price = { $lte: 20000 };
    } else if (price > 20000 && price <= 40000) {
      query.price = { $gt: 20000, $lte: 40000 };
    } else if (price > 40000 && price <= 60000) {
      query.price = { $gt: 40000, $lte: 60000 };
    } else if (price > 60000 && price <= 80000) {
      query.price = { $gt: 60000, $lte: 80000 };
    } else {
      query.price = { $gt: 80000 };
    }

    const documents = await Cars.find(query);
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Get cars by dealer ID and minimum year
app.get('/carsbyyear/:id/:year', async (req, res) => {
  try {
    const documents = await Cars.find({ 
      dealer_id: req.params.id, 
      year: { $gte: parseInt(req.params.year) } 
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});