The following is a guide to connect to our instance's website and database.

1. Run putty.exe

2. Host Name: 3.15.181.194
   Saved Session: 3.15.181.194

3. Connection -> SSH -> Tunnels
   Source Port: 8888
   Destination: localhost:80
   select "Add"

4. Connection -> SSH -> Auth, browse the following files in the zipped up    source code (NOT IN GITHUB REPOSITORY)
   spm.ppk

5. Go back to session and Save

6. Open the session

7. Enter user: bitnami
   Key passphrase: spmeasys

8. After successful log in.. cd to the following path using the following code
   cd htdocs/SPM/models/flask

9. Run the following code to activate the flask virt env with the following code
   source bin/activate

10. Return to previous path with the following code
    cd ..

11. Run a python file with following code
    python course.py

12. Duplicate and repeat step 7 to 11 for all python files listed below and ensure all are running.

    List of python file (ports: pythonfile)
    5001: course.py
    5002: engineer.py
    5003: learner_class.py
    5004: class.py
    5005: learner.py
    5006: trainer.py
    5007: lesson.py
    5008: material.py
    5010: quiz.py
    5011: quiz_question.py
    5012: learner_quiz.py
    5013: learner_lesson.py

13. To access database, go to http://127.0.0.1:8888/phpmyadmin and login with the following.

    username: root
    password: WxJJy9gTnsC9

14. To access websites, the following are the links.

    4 Core

    Engineer self-enrol into courses: http://3.15.181.194/SPM/ui/allCourses.html

    HR assign engineers into courses: http://3.15.181.194/SPM/ui/hr_enrol.html

    Learner take courses assigned: http://3.15.181.194/SPM/ui/course.html	

    Trainer create quiz for courses: http://3.15.181.194/SPM/ui/trainer_quiz.html

    General

    Learner: http://3.15.181.194/SPM/ui/index.html (allCourses, withdrawal, message)
             http://3.15.181.194/SPM/ui/course.html (access material, take quiz)

    HR: http://3.15.181.194/SPM/ui/hr.html (hr enrol, hr request, classlist, uncompleted learner)

    Trainer: http://3.15.181.194/SPM/ui/index_trainer.html (classlist, create quiz)