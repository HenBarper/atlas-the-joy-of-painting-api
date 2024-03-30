CREATE TABLE IF NOT EXISTS episodes (
    paintingIndex VARCHAR(10) NOT NULL UNIQUE PRIMARY KEY,
    title VARCHAR(255),
    season INT,
    episode INT,
    airDate DATE,
    notes VARCHAR(255),
    img_src VARCHAR(255),
    youtube_src VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS colors (
    colorID INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    colorName VARCHAR(50),
    hexValue VARCHAR(7)
);

CREATE TABLE IF NOT EXISTS subjects (
    subjectID INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    subjectName VARCHAR(255)
);

-- junction table
CREATE TABLE IF NOT EXISTS episode_colors (
    paintingIndex VARCHAR(10),
    colorID INT,
    FOREIGN KEY (paintingIndex) REFERENCES episodes(paintingIndex),
    FOREIGN KEY (colorID) REFERENCES colors(colorID),
    PRIMARY KEY (paintingIndex, colorID)
);

-- junction table
CREATE TABLE IF NOT EXISTS episode_subject (
    paintingIndex VARCHAR(10),
    subjectID INT,
    FOREIGN KEY (paintingIndex) REFERENCES episodes(paintingIndex),
    FOREIGN KEY (subjectID) REFERENCES subjects(subjectID),
    PRIMARY KEY (paintingIndex, subjectID)
);