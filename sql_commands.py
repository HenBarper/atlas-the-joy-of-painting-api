# All episodes with color_id 2
episode_by_color_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || colors || ',' LIKE '%,2,%';
  '''
)
# All episodes with multiple color ids(1,2,3)
episode_by_colors_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || colors || ',' LIKE '%,1,%'
    AND ',' || colors || ',' LIKE '%,2,%'
    AND ',' || colors || ',' LIKE '%,3,%';
  '''
)
# All episdes with color named Black Gesso
episodes_by_color_name_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || colors || ',' LIKE '%,' || 
      (SELECT color_id::varchar FROM colors WHERE color_name = 'Alizarin-Crimson') || ',%';
  '''
)
# All episodes with subject_id 2
episode_by_subject_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || subjects || ',' LIKE '%,2,%';
  '''
)
# All episodes with multiple subject ids(1,2,3)
episode_by_subjects_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || subjects || ',' LIKE '%,1,%'
    AND ',' || subjects || ',' LIKE '%,2,%'
    AND ',' || subjects || ',' LIKE '%,3,%';
  '''
)
# All episdes with subject beach
episodes_by_color_name_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || subjects || ',' LIKE '%,' || 
      (SELECT subject_id::varchar FROM subjects WHERE subject_name = 'Beach') || ',%';
  '''
)

# All episdoes by month(JANUARY)
episodes_by_month_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE month = 'January';
  '''
)

# BONUS REVERSE ---------------------------------------------------------------------
# All colors from episode with episode_id 4
colors_by_episode_query = (
  f'''
  SELECT cols.*
  FROM episodes eps
  JOIN colors cols ON ',' || eps.colors || ',' LIKE '%,' || cols.color_id || ',%'
  WHERE eps.episode_id = 4;
  '''
)
# All subjects from episode with episode_id 4
subjects_by_episode_query = (
  f'''
  SELECT subs.*
  FROM episodes eps
  JOIN subjects subs ON ',' || eps.subjects || ',' LIKE '%,' || subs.subject_id || ',%'
  WHERE eps.episode_id = 4;
  '''
)



