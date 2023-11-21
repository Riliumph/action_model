CREATE TABLE sample_app.scenario_loads(
    id serial NOT NULL,
    scenario_id integer NOT NULL,
    scenario_seq integer NOT NULL,
    pallet_id integer NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(scenario_id) REFERENCES sample_app.scenarios(scenario_id)
);
