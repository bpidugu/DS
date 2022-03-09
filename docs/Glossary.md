#  Software Key Terms
## ACID Transaction:
  
   
   ** Atomicity**: The operations that constitute the transaction will either
    all succeed or all fail. There is no in-between state.
 
    **Consistency**: The transaction cannot bring the database to an invalid
    state. After the transaction is committed or rolled back, the rules for each
    record will still apply, and all future transactions will see the effect of
    the transaction. Also named <b>Strong Consistency</b>.
  

