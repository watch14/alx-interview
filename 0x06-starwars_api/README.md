<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Alx Interview" />

  &#xa0;

  <!-- <a href="https://alxinterview.netlify.app">Demo</a> -->
</div>

<h2 align="center">Alx Interview</h2>


# Star Wars Characters Fetcher

This script fetches and displays the names of characters from a Star Wars movie using the Star Wars API (SWAPI).

## Prerequisites

- Node.js installed on your machine.

## Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/your-repository.git
```

Navigate to the directory containing the script.
Copy code
cd your-repository
Run the script with the desired movie ID as an argument.
```bash
./0-starwars_characters.js movie_id
```
Replace movie_id with the ID of the Star Wars movie you want to fetch characters from. For example:

```bash
./0-starwars_characters.js 1
```
This will fetch characters from Episode IV: A New Hope.

How It Works
The script makes an HTTP request to the SWAPI to fetch information about a particular Star Wars movie using its ID. It then retrieves the list of characters appearing in that movie and makes individual requests to fetch the names of each character. Once all character names are retrieved, it prints them to the console.




