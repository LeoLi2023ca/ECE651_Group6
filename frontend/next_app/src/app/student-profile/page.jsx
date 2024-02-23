"use client"
import React, { useState } from 'react';
import styles from "./studentProfile.module.css";
import StudentProfileHeader from "../../components/studentProfiles/StudentProfileHeader";
import StudentEdit from "@/components/studentProfiles/StudentEdit";
import StudentInfo from "@/components/studentProfiles/StudentInfo";
import StudentIntroduction from "@/components/studentProfiles/StudentIntroduction";
import StudentAim from "@/components/studentProfiles/StudentAim";



const StudentProfilePage = () => {

    const [studentData, setStudentData] = useState({
        name: "John Doe",
        avatarUrl: "https://bpic.51yuansu.com/pic3/cover/04/06/00/65901191b4b91_800.jpg?x-oss-process=image/sharpen,100",
        subject : "Physics",
        tagline : "Physics to 90",
        level: "High School",
        grade: " 10 ",
        studyTime: "10",
        school: "Henan Experimental High School",
        email : "j65fan@uwaterloo.ca",
        introText: "Long introduction text goes here...",
        aim: "Long Aim of This study goes here",
    });

    const [isEditMode, setIsEditMode] = useState(false);

    const handleProfileUpdate = (updatedProfile) => {
        setStudentData(updatedProfile);
        setIsEditMode(false);
    };

    const toggleEditMode = () => {
        setIsEditMode(!isEditMode);
    };


    return (
        <div className={styles.pageContainer}>
            <div className={styles.header}>
            </div>
            <div className={styles.mainContent}>
                <div className={styles.leftColumn}>
                    <StudentProfileHeader
                        name={studentData.name}
                        avatarUrl={studentData.avatarUrl}
                        subject={studentData.subject}
                        tagline={studentData.tagline}
                    />

                    <StudentEdit userProfile={studentData} onUpdate={handleProfileUpdate} onToggleEditMode={toggleEditMode} />

                    {/* visible or invisible */}
                    {!isEditMode && (
                        <>
                            <StudentInfo
                                education={studentData.highestDegree}
                                school={studentData.graduatedFrom}
                                grade={studentData.grade}
                                studyTime={studentData.studyTime}
                                email={studentData.email}
                            />
                            <StudentIntroduction introText={studentData.introText}/>
                            <StudentAim lessonInfo={studentData.aim}/>
                        </>
                    )}
                </div>
            </div>
        </div>
    );
};

export default StudentProfilePage;