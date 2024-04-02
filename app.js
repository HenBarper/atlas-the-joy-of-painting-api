const express = require('express');
const { Pool } = require('pg');
  
const app = express(); 
const PORT = 3000;

const pool = new Pool({
  user: 'postgres',
  host: '127.0.0.1',
  database: 'mydb',
  password: 'p0$tGR3z',
  port: '5432', // default PostgreSQL port
});

// ALL EPISODES ----------------------------------------------------------------------
app.get('/episodes', async (req, res) => {
  try {
    // Execute a query to fetch data from the database
    const queryResult = await pool.query('SELECT * FROM episodes')

    // Send the fetched data as the response
    res.json(queryResult.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// ALL COLORS ----------------------------------------------------------------------
app.get('/colors', async (req, res) => {
  try {
    // Execute a query to fetch data from the database
    const queryResult = await pool.query('SELECT * FROM colors')

    // Send the fetched data as the response
    res.json(queryResult.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// ALL SUBJECTS ----------------------------------------------------------------------
app.get('/subjects', async (req, res) => {
  try {
    // Execute a query to fetch data from the database
    const queryResult = await pool.query('SELECT * FROM subjects')

    // Send the fetched data as the response
    res.json(queryResult.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// All episodes by color id ----------------------------------------------------------
app.get('/color_id/:color_id', async (req, res) => {
  const color_id = req.params.color_id;
  try {
    // Execute a query to fetch data from the database
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || colors || ',' LIKE $1`,
      values: [`%,${color_id},%`],
    };

    // Execute the query
    const result = await pool.query(query);

    // Send the response
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// All episdes with color-name ---------------------------------------------------------
app.get('/color_name/:color_name', async (req, res) => {
  const color_name = req.params.color_name;
  try {
    // Execute a query to fetch data from the database
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || colors || ',' LIKE '%,' || (SELECT color_id::varchar FROM colors WHERE color_name = $1) || ',%';`,
      values: [color_name],
    };
    console.log(query);
    // Execute the query
    const result = await pool.query(query);

    // Send the response
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
  console.log('end');
});

// All episodes by subject id ----------------------------------------------------------
app.get('/subject_id/:subject_id', async (req, res) => {
  const subject_id = req.params.subject_id;
  try {
    // Execute a query to fetch data from the database
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || subjects || ',' LIKE $1`,
      values: [`%,${subject_id},%`],
    };

    // Execute the query
    const result = await pool.query(query);

    // Send the response
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// All episdes with subject-name ---------------------------------------------------------
app.get('/subject_name/:subject_name', async (req, res) => {
  const subject_name = req.params.subject_name;
  try {
    // Execute a query to fetch data from the database
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || subjects || ',' LIKE '%,' || (SELECT subject_id::varchar FROM subjects WHERE subject_name = $1) || ',%';`,
      values: [subject_name],
    };
    console.log(query);
    // Execute the query
    const result = await pool.query(query);

    // Send the response
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
  console.log('end');
});


app.listen(PORT, (error) =>{ 
  if(!error) 
    console.log("Server is Successfully Running, and App is listening on port "+ PORT) 
  else 
    console.log("Error occurred, server can't start", error); 
  }
);