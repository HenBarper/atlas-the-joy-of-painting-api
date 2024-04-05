const express = require('express');
const fs = require('fs');
const { Pool } = require('pg');
  
const app = express();
app.use(express.static('./'));
const PORT = 3000;

const pool = new Pool({
  user: 'postgres',
  host: '127.0.0.1',
  database: 'mydb',
  password: 'p0$tGR3z',
  port: '5432', // default PostgreSQL port
});

// Routes -----------------------------------------------------------------------------------------------------------------------

// Base HTML
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// All Episodes HTML
app.get('/episodes', async (req, res) => {
  try {
    const queryResult = await pool.query(`
      SELECT e.*, array_agg(DISTINCT c.color_name) AS color_names, array_agg(DISTINCT s.subject_name) AS subject_names
      FROM episodes e
      LEFT JOIN colors c ON c.color_id = ANY(string_to_array(e.colors, ',')::int[])
      LEFT JOIN subjects s ON s.subject_id = ANY(string_to_array(e.subjects, ',')::int[])
      GROUP BY e.episode_id
    `);
    
    const episodes = queryResult.rows;
    let episodeHTML = '';

    episodes.forEach(episode => {
      episodeHTML += `
        <div id="${episode.episode_id}">
          <h2>${episode.episode_id}. ${episode.title}</h2>
          <p>season ${episode.season}, episode${episode.episode} - Original Air Date: ${episode.air_date}</p>
          ${episode.notes ? `<p>${episode.notes}</p>` : ''}
          <img src="${episode.image_src}" alt="${episode.title}">
          <p>Colors: ${episode.color_names.join(', ')}</p>
          <p>Subject matter: ${episode.subject_names.join(', ')}</p>
          <a href="${episode.youtube_src}">Youtube - ${episode.title}</a>
          <hr>
        </div>
      `;
    });

    // Read the content of paintings.html and append episodeHTML
    fs.readFile(__dirname + '/paintings.html', 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading file', err);
        res.status(500).send('Internal Server Error');
        return;
      }

      const modifiedHTML = data.replace('</body>', episodeHTML + '</body>');
      res.send(modifiedHTML);
    });
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).send('Internal Server Error');
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
// All episodes with color-name
app.get('/color_name/:color_name', async (req, res) => {
  const color_name = req.params.color_name;
  try {
    // Execute a query to fetch data from the database
    const queryResult = await pool.query(`
      SELECT e.*, 
             string_agg(DISTINCT c.color_name, ', ') AS color_names, 
             string_agg(DISTINCT s.subject_name, ', ') AS subject_names
      FROM episodes e
      LEFT JOIN colors c ON c.color_id = ANY(string_to_array(e.colors, ',')::int[])
      LEFT JOIN subjects s ON s.subject_id = ANY(string_to_array(e.subjects, ',')::int[])
      WHERE ',' || e.colors || ',' LIKE '%,' || (SELECT color_id::varchar FROM colors WHERE color_name = $1) || ',%'
      GROUP BY e.episode_id
    `, [color_name]);

    const episodes = queryResult.rows;
    let episodeHTML = '';

    episodes.forEach(episode => {
      episodeHTML += `
        <div id="${episode.episode_id}">
          <h2>${episode.episode_id}. ${episode.title}</h2>
          <p>season ${episode.season}, episode ${episode.episode} - Original Air Date: ${episode.air_date}</p>
          ${episode.notes ? `<p>${episode.notes}</p>` : ''}
          <img src="${episode.image_src}" alt="${episode.title}">
          <p>Colors: ${episode.color_names}</p>
          <p>Subject matter: ${episode.subject_names}</p>
          <a href="${episode.youtube_src}">Youtube - ${episode.title}</a>
          <hr>
        </div>
      `;
    });

    // Read the content of paintings.html and append episodeHTML
    fs.readFile(__dirname + '/paintings.html', 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading file', err);
        res.status(500).send('Internal Server Error');
        return;
      }

      const modifiedHTML = data.replace('</body>', episodeHTML + '</body>');
      res.send(modifiedHTML);
    });
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).send('Internal Server Error');
  }
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
// All episodes with subject-name
app.get('/subject_name/:subject_name', async (req, res) => {
  const subject_name = req.params.subject_name;
  try {
    // Execute a query to fetch data from the database
    const queryResult = await pool.query(`
      SELECT e.*, 
             string_agg(DISTINCT c.color_name, ', ') AS color_names, 
             string_agg(DISTINCT s.subject_name, ', ') AS subject_names
      FROM episodes e
      LEFT JOIN colors c ON c.color_id = ANY(string_to_array(e.colors, ',')::int[])
      LEFT JOIN subjects s ON s.subject_id = ANY(string_to_array(e.subjects, ',')::int[])
      WHERE ',' || e.subjects || ',' LIKE '%,' || (SELECT subject_id::varchar FROM subjects WHERE subject_name = $1) || ',%'
      GROUP BY e.episode_id
    `, [subject_name]);

    const episodes = queryResult.rows;
    let episodeHTML = '';

    episodes.forEach(episode => {
      episodeHTML += `
        <div id="${episode.episode_id}">
          <h2>${episode.episode_id}. ${episode.title}</h2>
          <p>season ${episode.season}, episode ${episode.episode} - Original Air Date: ${episode.air_date}</p>
          ${episode.notes ? `<p>${episode.notes}</p>` : ''}
          <img src="${episode.image_src}" alt="${episode.title}">
          <p>Colors: ${episode.color_names}</p>
          <p>Subject matter: ${episode.subject_names}</p>
          <a href="${episode.youtube_src}">Youtube - ${episode.title}</a>
          <hr>
        </div>
      `;
    });

    // Read the content of paintings.html and append episodeHTML
    fs.readFile(__dirname + '/paintings.html', 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading file', err);
        res.status(500).send('Internal Server Error');
        return;
      }

      const modifiedHTML = data.replace('</body>', episodeHTML + '</body>');
      res.send(modifiedHTML);
    });
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).send('Internal Server Error');
  }
});


// All episdes by Month ---------------------------------------------------------
// All episodes by Month
app.get('/month/:month_name', async (req, res) => {
  const month_name = req.params.month_name;
  try {
    // Execute a query to fetch data from the database
    const queryResult = await pool.query(`
      SELECT e.*, 
             string_agg(DISTINCT c.color_name, ', ') AS color_names, 
             string_agg(DISTINCT s.subject_name, ', ') AS subject_names
      FROM episodes e
      LEFT JOIN colors c ON c.color_id = ANY(string_to_array(e.colors, ',')::int[])
      LEFT JOIN subjects s ON s.subject_id = ANY(string_to_array(e.subjects, ',')::int[])
      WHERE e.month = $1
      GROUP BY e.episode_id
    `, [month_name]);

    const episodes = queryResult.rows;
    let episodeHTML = '';

    episodes.forEach(episode => {
      episodeHTML += `
        <div id="${episode.episode_id}">
          <h2>${episode.episode_id}. ${episode.title}</h2>
          <p>season ${episode.season}, episode ${episode.episode} - Original Air Date: ${episode.air_date}</p>
          ${episode.notes ? `<p>${episode.notes}</p>` : ''}
          <img src="${episode.image_src}" alt="${episode.title}">
          <p>Colors: ${episode.color_names}</p>
          <p>Subject matter: ${episode.subject_names}</p>
          <a href="${episode.youtube_src}">Youtube - ${episode.title}</a>
          <hr>
        </div>
      `;
    });

    // Read the content of paintings.html and append episodeHTML
    fs.readFile(__dirname + '/paintings.html', 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading file', err);
        res.status(500).send('Internal Server Error');
        return;
      }

      const modifiedHTML = data.replace('</body>', episodeHTML + '</body>');
      res.send(modifiedHTML);
    });
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).send('Internal Server Error');
  }
});


// End of routes -----------------------------------------------------------------------------------------------------

app.listen(PORT, (error) =>{ 
  if(!error) 
    console.log("Server is Successfully Running, and App is listening on port "+ PORT) 
  else 
    console.log("Error occurred, server can't start", error); 
  }
);

// DEPRECATED

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

// All episodes by color name
app.get('/color_name/:color_name', async (req, res) => {
  const color_name = req.params.color_name;
  try {
    // Execute a query to fetch data from the database
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || colors || ',' LIKE '%,' || (SELECT color_id::varchar FROM colors WHERE color_name = $1) || ',%';`,
      values: [color_name],
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
// app.get('/subject_name/:subject_name', async (req, res) => {
//   const subject_name = req.params.subject_name;
//   try {
//     // Execute a query to fetch data from the database
//     const query = {
//       text: `SELECT * FROM episodes WHERE ',' || subjects || ',' LIKE '%,' || (SELECT subject_id::varchar FROM subjects WHERE subject_name = $1) || ',%';`,
//       values: [subject_name],
//     };
//     // Execute the query
//     const result = await pool.query(query);

//     // Send the response
//     res.json(result.rows);
//   } catch (error) {
//     console.error('Error executing query', error);
//     res.status(500).json({ message: 'Internal Server Error' });
//   }
// });

// All episdes by Month ---------------------------------------------------------
// app.get('/month/:month_name', async (req, res) => {
//   const month_name = req.params.month_name;
//   try {
//     // Execute a query to fetch data from the database
//     const query = {
//       text: `SELECT * FROM episodes WHERE month = $1;`,
//       values: [month_name],
//     };
//     // Execute the query
//     const result = await pool.query(query);

//     // Send the response
//     res.json(result.rows);
//   } catch (error) {
//     console.error('Error executing query', error);
//     res.status(500).json({ message: 'Internal Server Error' });
//   }
// });