# Pokemon-Partner-Project
This is my Partner Project I worked on with Louis
Our Addtional Features Are:
- Streamlit UI (should count as 2)
- Images in UI for Pokemon
- Addtional Pokemon/Moves for Leveling Up/Evolution
- Battle Again Feature
- Balancing for opponents
- Capture chance (50%)
- (wanted to have status moves but ran out of time so they just have 0 power and are basically placeholders)
  
This link should take you to where the app is being hosted and you can play it there https://pokemon-partner-project-k4ryhct2xmaasyxpmgtzkj.streamlit.app/ . However, I have not published anything before on Streamlit so I am unsure if it will work at all or as intended.

Make sure to check the requirements section to run it on your own computer.
To run streamlit, run the code noramlly, then in the terminal enter streamlit run /Users/USER/Pokemon_Project.py or which ever directory it is stored in and named.

Addtionally, the program does not pass all PEP8 standards since streamlit causes lines to be overly long and also while working on vscode, the lines didnt seem overly long (most of the time). Addtionally, the blank lines between code blocks are different from PEP8 standards because, for this project, they made it far more clear and organized.

Streamlit is a module for Python which allows for the creation of apps on webpages, we used it only to open a browser window for our UI. Many of the parts of streamlit are intuitive like st.write writing something on the website. However, streamlit becomes very complicated when managing inputs. To gather inputs form a user you (most of the time) have to use a form with a unique key and use. Then, streamlit dosent actually stop and wait for user inputs. To fix this, we used st.stop() to stop streamlit form continuing to run and st.rerun to rerun the program. This works because streamlit has its own system of storing vairables. Streamlit uses st.session.state to store any type of variable or data. This allows variables to persist across streamlit even when everything is stopped and reran. This basically allowed us to keep variables while the program reran after user inputs. This also makes it so we don't have to use loops for anything.
If you have any questions let me know!
