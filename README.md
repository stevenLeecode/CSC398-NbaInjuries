# CSC398-NbaInjuries

#### Author Wilkenson H.
Following this will only show the dataprocessing step 

1. In the root directory creave a venv folfer and activate it 
 
  - for mac OS 
    ```bash
    RUN python3 -m venv venv
    RUN source venv/bin/activate 

2. Verify that there is a .gitignore file and the venv folder is in it 

3.  From the terminal where the venv folder is and the requirements.txt are (to install all the dependencies need to run the program)
    ```bash 
    RUN python3 install -r requirements.txt
    ```
4. In the terminal root folder same location as the main.py file 
    ```bash
    RUN streamlit run main.py
    ```

5. To see the processed data navgate to classifier folder 
uncomment these lines of code 
```python
# player_data = pd.read_csv('final_player_data.csv') 

# print(player_data.head())
```

```bash
RUN python3 knn.py
```
This comment will show u a snapshot of the data in the terminal



    


