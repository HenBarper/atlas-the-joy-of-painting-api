CREATE TABLE "episodes" (
  "episode_id" integer PRIMARY KEY,
  "title" varchar,
  "season" integer,
  "episode" integer,
  "colors" varchar,
  "subjects" varchar,
  "air_date" varchar,
  "month" varchar,
  "notes" varchar,
  "image_src" varchar,
  "youtube_src" varchar
);

CREATE TABLE "subjects" (
  "subject_id" integer PRIMARY KEY,
  "subject_name" varchar
);

CREATE TABLE "colors" (
  "color_id" integer PRIMARY KEY,
  "color_name" varchar
);

-- Join table
CREATE TABLE "episode_subjects" (
  "episode_id" integer,
  "subject_id" integer,
  PRIMARY KEY("episode_id", "subject_id")
);
ALTER TABLE "episode_subjects" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episode_subjects" ADD FOREIGN KEY ("subject_id") REFERENCES "subjects" ("subject_id");

-- Join Table
CREATE TABLE "episode_colors" (
  "episode_id" integer,
  "color_id" integer,
  PRIMARY KEY("episode_id", "color_id")
);
ALTER TABLE "episode_colors" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episode_colors" ADD FOREIGN KEY ("color_id") REFERENCES "colors" ("color_id");
