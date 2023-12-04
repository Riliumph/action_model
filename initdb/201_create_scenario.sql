CREATE TABLE sample_app.scenarios(
    scenario_id serial PRIMARY KEY,
    scenario_name text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP
);
