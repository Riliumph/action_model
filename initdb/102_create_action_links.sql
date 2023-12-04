CREATE TABLE sample_app.action_links(
    action_link_id serial PRIMARY KEY,
    root_action_id integer NOT NULL,
    seq integer NOT NULL,
    action_id integer NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(root_action_id) REFERENCES sample_app.actions (action_id),
    FOREIGN KEY(action_id) REFERENCES sample_app.actions (action_id),
    UNIQUE(root_action_id, seq)
);

INSERT INTO
    sample_app.action_links(
        root_action_id,
        seq,
        action_id
    )
VALUES
    -- ユースケース1
    (1, 1, 2),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 4),
    (1, 5, 5);
