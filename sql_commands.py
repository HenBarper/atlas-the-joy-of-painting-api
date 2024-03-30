# All episodes with color_id
color_id = 2
episode_by_color_query = (
  f'''
  SELECT *
  FROM episodes
  WHERE ',' || colors || ',' LIKE '%,{color_id},%';
  '''
)

# All colors from episode with episode_id
episode_id = 4
colors_by_episode_query = (
  f'''
  SELECT c.*
  FROM episodes e
  JOIN colors c ON ',' || e.colors || ',' LIKE '%,' || c.color_id || ',%'
  WHERE e.episode_id = {episode_id};
  '''
)



