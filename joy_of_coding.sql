CREATE TABLE "colors" (
  "color_id" integer PRIMARY KEY,
  "name" varchar,
  "hexcode" varchar,
  "episode_id" integer
);

CREATE TABLE "subjects" (
  "subject_id" integer PRIMARY KEY,
  "subject" varchar,
  "episode_id" integer
);

CREATE TABLE "episodes" (
  "episode_id" integer PRIMARY KEY,
  "title" varchar,
  "season" integer,
  "episode" integer,
  "num_colors" integer,
  "colors" varchar,
  "subjects" varchar,
  "air_date" varchar,
  "month" integer,
  "notes" varchar,
  "image_src" varchar,
  "youtube_src" varchar
);

CREATE TABLE "episodes_colors" (
  "episodes_colors" varchar,
  "colors_color_id" integer,
  PRIMARY KEY ("episodes_colors", "colors_color_id")
);

ALTER TABLE "episodes_colors" ADD FOREIGN KEY ("episodes_colors") REFERENCES "episodes" ("colors");

ALTER TABLE "episodes_colors" ADD FOREIGN KEY ("colors_color_id") REFERENCES "colors" ("color_id");


CREATE TABLE "episodes_subjects" (
  "episodes_subjects" varchar,
  "subjects_subject_id" integer,
  PRIMARY KEY ("episodes_subjects", "subjects_subject_id")
);

ALTER TABLE "episodes_subjects" ADD FOREIGN KEY ("episodes_subjects") REFERENCES "episodes" ("subjects");

ALTER TABLE "episodes_subjects" ADD FOREIGN KEY ("subjects_subject_id") REFERENCES "subjects" ("subject_id");


CREATE TABLE "subjects_episodes" (
  "subjects_episode_id" integer,
  "episodes_episode_id" integer,
  PRIMARY KEY ("subjects_episode_id", "episodes_episode_id")
);

ALTER TABLE "subjects_episodes" ADD FOREIGN KEY ("subjects_episode_id") REFERENCES "subjects" ("episode_id");

ALTER TABLE "subjects_episodes" ADD FOREIGN KEY ("episodes_episode_id") REFERENCES "episodes" ("episode_id");


CREATE TABLE "colors_episodes" (
  "colors_episode_id" integer,
  "episodes_episode_id" integer,
  PRIMARY KEY ("colors_episode_id", "episodes_episode_id")
);

ALTER TABLE "colors_episodes" ADD FOREIGN KEY ("colors_episode_id") REFERENCES "colors" ("episode_id");

ALTER TABLE "colors_episodes" ADD FOREIGN KEY ("episodes_episode_id") REFERENCES "episodes" ("episode_id");

