# CS IA | Baybai: a Baybayin script learning app


# Criteria A: Planning
## Problem Definition
Baybayin (ᜊᜌ᜔ᜊᜌᜒᜈ᜔) is one of the precolonial writing systems used by early Filipinos as the writing component of Tagalog (the national language of the Philippines). More than three centuries of Spanish colonization led to the replacement of Baybayin by the Latin alphabet.

A teacher in a public high school in the Philippines aims to revive Baybayin by teaching the script to his students. Given that teaching Baybayin is not part of the national curriculum and therefore is not allotted time, learning outside of class is vital. The client has tried to implement such kind of learning through homeworks, and a list of links of references but all to no avail. To add, internet and desktop access pose challenges as they are not readily available due to the costs associated with mobile data plans, Wi-Fi, and laptops. Students struggle to retain the script outside the classroom, given its limited usage outside a specific niche. The teacher emphasizes the importance of consistency in learning Baybayin, highlighting the need for an app that encourages regular practice. Additionally, a translator feature is essential for students to apply the script in real-life contexts. Furthermore, like any language, growth (through objective assessment & working on gaps ) and consistent practice involving writing and memorizing characters are crucial for effective learning.

*<a href="#ap-a">Refer to Appendix A for client interview proof</a>*

## Proposed Solution
The proposed solution to address the challenges faced by the teacher and students in learning Baybayin is a mobile application called 'Baybai'. The application gets it name from the root word of 'Baybayin' which is 'baybay' meaning 'to spell' and 'bai' a Filipino expression which means friend. 'Baybai' is designed to provide an accessible and engaging platform for learning the Baybayin script. Developed using Python and KivyMD and the database handled using SQLite, the app allows students to conveniently learn and practice Baybayin outside the classroom. It offers a comprehensive learning experience with interactive lessons, flashcards, and writing practice exercises. The app incorporates a spaced repetition system to ensure optimal retention and growth in learning. To address the limitations of internet and desktop access, 'baybai' operates offline, enabling students to learn without relying on costly data plans or Wi-Fi. The app includes a translator feature that allows users to easily translate Tagalog words and phrases into Baybayin characters, facilitating practical application in real-life contexts. Furthermore, 'baybai' tracks and measures students' progress through objective assessments, providing them with a clear understanding of their proficiency level and motivating them to strive for continuous improvement. With its user-friendly interface, comprehensive learning resources, and focus on consistency and growth, 'baybai' empowers students to revive and master the Baybayin script effectively.

## Rationale for Proposed Solution

**Mobile Application**
* Accessibility: A mobile application ensures widespread accessibility for students, as mobile phones are the most accessible gadgets for them, considering factors like cost and availability of internet access[^1]. Mobile phones can also be accessed anytime, anywhere making it an on-the-go learning aid.

**Flashcards-Based Learning**
* Effective Learning Technique: Flashcards are known for their effectiveness in promoting active recall and spaced repetition, aiding in long-term retention and comprehension (source: Association for Psychological Science)[^2].
* Visual and Engaging: Flashcards provide visual cues, helping students associate Baybayin characters with their meanings, making the learning process more engaging and memorable[^2].

**Python and Kivy**
* Cross-Platform Compatibility: Python, a versatile programming language, along with Kivy, a Python framework, allows for the development of cross-platform mobile applications, ensuring compatibility across various operating systems[^3],[^4].


**PyCharm**
* Python-Specific Support: PyCharm offers dedicated support for Python development, including syntax highlighting, code analysis, and refactoring tools, which contribute to the smooth development process and code quality[^5].

**SQLite**
* Efficient and Reliable: SQLite offers high-performance data storage and retrieval capabilities, ensuring smooth data management within the mobile application, including user progress tracking and storing translation data[^6].

## Design Statement
I will design and make a mobile application for a client who is a Tagalog teacher at a public high school in the Philippines. The application will allow users to learn Baybayin and have three main functionalities: learning mode, test mode, and translator. It will be developed using the Python programming language, KivyMD, and the PyCharm Integrated Development Environment. It will take 8 weeks to make and will be evaluated according to the following success criteria.


## Success Criteria

| No. | Success Criteria                                                                                                                                                                    | Issue Tackled                                                                                           |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| 1   | The app allows the user to set a daily goal of flashcards to be read. The app then keeps track on whether the user has reached that goal for the day or not.                        | "...highlighting the need for an app that encourages regular practice."                                 |
| 2   | The flashcards in Learning Mode shows Baybayin characters and its corresponding Tagalog translation.                                                                                | "...consistent practice involving writing and memorizing characters is crucial for effective learning." |                                                                                                                                                                
| 3   | The Test Mode will assess users' knowledge and proficiency in Baybayin. It will generate random Tagalog words, challenging users to type in the corresponding Baybayin script.      | "...growth (through objective assessment & working on gaps)...are crucial for effective learning."      |
| 4   | Scores gained from Test Mode will be recorded, with the respective date & time the test was taken. The user is then able to see their scores or progress visualized through a graph. | "...growth (through objective assessment & working on gaps)...are crucial for effective learning."      |
| 5   | The app allows the user to 'star' or save a flashcard for later reference or memorization.                                                                                          | "...growth (through objective assessment & working on gaps)...are crucial for effective learning."      |
| 6   | The app enables Tagalog to Baybayin translation and allows the user to copy the Baybayin characters to their clipboard.                                                             | "It's important for students to have a translator to apply the script in real-life context."            |
| 7   | The app allows users to copy the Baybayin script to their clipboard                                                                                                                 | "It's important for students to have a translator to apply the script in real-life context."            |
| 8   | The solution has a registration and log in system.                                                                                                                                  |                                                                                                         |
| 9   | The app contains a social network option so users can interact with other users who want to learn Baybayin.                                                                         |                                                                                                         |




# Criteria B: Design
## Diagrams
### System Diagrams
### Wireframes
![](docu/ui_draft.png)
Figure 1. Draft of the application's user interface created on Adobe XD


![](docu/wireframe.png)
Figure 2. Wireframe of the mobile application
### UML Diagram
### ER Diagram
### Flowcharts

## Record of Tasks
| Task No | Planned Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Planned Outcome                                                                                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Identify & interview the client                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                 | 6 min         | Jun 9                  | A         |
| 2       | Write the context of the problem                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Establish the problem identified in a clear and concise manner. The problem definition must include who the client is, what the client wants, and indicate a possible solution. | 15 min        | Jun 9                  | A         |
| 3       | Brainstorm and write a proposed solution for the problem. Rationalize this solution for the client.                                                                                                                                                                                                                                                                                                                                                                                            | Explain in a concise and clear manner the purpose of the project to the client                                                                                                  | 5 min         | Jun 9                  | A         |
| 4       | Write the success criteria of the proposed solution.                                                                                                                                                                                                                                                                                                                                                                                                                                           | A clear set standards to be met by the developer, that suits the client's needs and preferences.                                                                                | 15 min        | Jun 10                 | A         |
| 5       | Meet with the client to confirm or revise success criteria.                                                                                                                                                                                                                                                                                                                                                                                                                                    | Confirmed success criteria and ensure it meets the client's standards.                                                                                                          | 15 min        | Jun 10                 | A         |
| 6       | Write a design statement for the proposed solution 'spent.io'                                                                                                                                                                                                                                                                                                                                                                                                                                  | A coherent design statement that outlines the plan for the project.                                                                                                             | 20 min        | Jun 10                 | A         |
| 7       | Draw a system diagram for the proposed app solution: 'spent.io'                                                                                                                                                                                                                                                                                                                                                                                                                                | Have a concrete idea of the software and hardware requirements involved in the development of the application.                                                                  | 10 min        | Jun 10                 | B         |
| 8       | Plan & create the wireframe for the proposed solution: 'spent.io'. The wireframe includes 3 screens: Login Screen, Registration Screen, and Main Screen. This wireframe plan must include the widgets to be shown, components (ex. Dialog, MDButton), dimensions of each screens, components, and color schemes. This must also outline the transition from one screen to another and how this is done. More importantly, the planned wireframe must align with the client's success criteria. | Have a detailed visual representation of the project which also serves as a guide for the developer during the programming process.                                             | 60 min        | Jun 11                 | B         |
| 9       | Develop Translation function back-end.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Have a 'Translator' function that receives a Tagalog word, syllabicates the word based on Tagalog language guidelines, and translates and returns the word to Baybayin script.  | 80 min        | Jul 21                 | C         |
| 10      | Develop Translation Mode (front and back-end)                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                 | 80 min        | Jul 22                 | C         |

## Test Plan
| Test No | Test Type                                                                                            | Date  | Procedure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Expected Outcome                                                                                                                                                                                                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| 1       | Functional: Test  whether the SignUp screen succesfully registers new user if all entries are valid. | Oct 8 | Run python file (spentio.py). Go to sign up screen and enter the following values: <br/>- email: bob@isak<br/>- username: bob<br/>-password: bob123                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | When the database, spentio.db is checked, a new row of data can be seen. This row shows the entered email, username, and password encrypted using a certain hash.                                                                                                                                   |
| 2       | Translation: Test the translation function.                                                          | Oct 8 | Using a Kaggle database from the University of the Philippines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                     |



# Appendix
## <a id="ap-a"> Appendix A. Client Interview </a>
![](docu/email_1.png)
![](docu/twt1.jpg)
![](docu/twt2.jpg)


# Sources
[^1]: https://kinsta.com/mobile-vs-desktop-market-share/#:~:text=To%20look%20at%20a%20similar,%2C%20and%202%25%20from%20tablet.
[^2]: https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.1537
[^3]: https://www.researchgate.net/publication/274572185_Comparative_Studies_of_Six_Programming_Languages
[^4]: https://kivy.org/
[^5]: https://www.jetbrains.com/pycharm/
[^6]: https://www.sqlite.org/inmemorydb.html

