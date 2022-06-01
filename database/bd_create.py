import psycopg2

conn = psycopg2.connect(dbname='postgres', user='wasd64',
                            password='', host='localhost')
cursor = conn.cursor()                            


cursor.execute(f'CREATE TABLE public.detect\
                    (\
                    frame_idx text,\
                    id text,\
                    bbox_left text,\
                    bbox_top text,\
                    bbox_w text,\
                    bbox_h text\
                    );')
conn.commit()