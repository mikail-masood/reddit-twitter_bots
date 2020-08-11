rom typing import List, Dict, Tuple
import sqlite3
import numpy as np
from matplotlib import pyplot as plt

def run_query(db: str, db_query: str, args: tuple = None) -> List[tuple]:
    '''Return the results of running query db_query on database with name db.
    Optional query arguments for can be included in args.
    '''
    
    con = sqlite3.connect(db)
    cur = con.cursor()
    
    if args is None: 
        cur.execute(db_query)
    else:
        cur.execute(db_query, args)

    data = cur.fetchall()
    cur.close()
    con.close()
    return data

