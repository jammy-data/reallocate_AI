# Reallocate T5.3 dashboard setup - data visualisation tool
The aim of this dashboard is to connect with the matchmaking tool designed by CERTH. To use this tool, there are a few prerequisites outlined below.

## 📁 Project Structure

- `notebooks/` - This contains jupyter notebooks designed for API data extraction, data exploration and initial data visualisation.
- `pages/`- Within this file we have the pages associated with the streamlit app.
- `Home.py` - This is our main streamlit page. This takes us to the homepage of the streamlit app.

## ⚙️ Setup

### 1 Install Dependencies

Create and set up a **virtual environment** using `uv`:

```sh
uv sync
```

### 2 Activate the Environment

```sh
source .venv/bin/activate
```

### 3 Aquire a BCN opendata portal API KEY

You will need to create a developer account [here](https://opendata-ajuntament.barcelona.cat/en/user/login?redirect=http://opendata-ajuntament.barcelona.cat/en/tokens)

once you have the API key. You will need to add it to the `.env.example` file in this repository, and then rename this file to `.env`

To do this in shell run ```sh cp .env.example .env ```

### 4 Run streamlit app

Install the package in editable mode (recommended):

```sh
uv pip install -e .
```

This project was create with uv.