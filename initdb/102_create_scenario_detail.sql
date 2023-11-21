CREATE TABLE sample_app.scenario_details(
    scenario_detail_id serial NOT NULL,
    scenario_id integer NOT NULL,
    scenario_seq integer NOT NULL,
    seq integer NOT NULL,
    p_key text NOT NULL,
    p_value text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scenario_id) REFERENCES sample_app.scenarios (scenario_id),
    UNIQUE(scenario_id, scenario_seq, p_key, p_value)
);
