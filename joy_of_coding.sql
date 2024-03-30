CREATE TABLE "colors" (
  "color_id" integer PRIMARY KEY,
  "color_name" varchar
);

CREATE TABLE "subjects" (
  "subject_id" integer PRIMARY KEY,
  "subject_name" varchar
);

CREATE TABLE "episodes" (
  "episode_id" integer PRIMARY KEY,
  "title" varchar,
  "season" integer,
  "episode" integer,
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

