CREATE TABLE sample_app.scenario_unloads(
    id serial PRIMARY KEY,
    scenario_id integer NOT NULL,
    scenario_seq integer NOT NULL,
    x integer NOT NULL,
    y integer NOT NULL,
    z integer NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(scenario_id) REFERENCES sample_app.scenarios(scenario_id)
);
