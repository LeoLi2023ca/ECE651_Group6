import React, { useState } from "react";
import Head from "next/head";
import styles from "./studentSearchBox.module.css";

const StudentSearchBox = () => {
    const [grade, setGrade] = useState('');
    const [subjects, setSubjects] = useState([]);
    const [language, setLanguage] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Form submitted with grade:', grade, ', language:', language);
    };

    const handleGradeChange = (event) => {
        const selectedGrade = event.target.value;
        setGrade(selectedGrade);

        const subjectsByGrade = {
            "kindergarten": ["Basic Math", "Reading Skills", "Others"],
            "elementary school": ["Math", "Science", "English Literature", "Others"],
            "middle school": ["Algebra", "Biology", "English", "Others"],
            "high school": ["Calculus", "Physics", "English Literature", "History", "Others"],
            "undergraduate program": ["Engineering", "Psychology", "Business Administration", "Others"],
            "graduate program": ["MBA", "Law", "Medicine", "Others"]
        };

        setSubjects(subjectsByGrade[selectedGrade] || []);
    };

    const handleLanguageChange = (event) => {
        setLanguage(event.target.value);
    };

    return (
        <div className={styles.container}>
            <Head>
                <title>Search Box</title>
            </Head>
            <div className={styles.searchBox}>
                <form onSubmit={handleSubmit}>
                    <label className={styles.label} htmlFor="grade-select">Grade</label>
                    <select className={styles.select} id="grade-select" name="grade" onChange={handleGradeChange} value={grade}>
                        <option value="">Select Grade</option>
                        <option value="kindergarten">Kindergarten</option>
                        <option value="elementary school">Elementary School</option>
                        <option value="middle school">Middle School</option>
                        <option value="high school">High School</option>
                        <option value="undergraduate program">Undergraduate Program</option>
                        <option value="graduate program">Graduate Program</option>
                    </select>

                    <label className={styles.label} htmlFor="subject-select">Subjects</label>
                    <select className={styles.select} id="subject-select" name="subject">
                    <option value="">Select Subjects</option>
                        {subjects.map((subject, index) => (
                            <option key={index} value={subject}>{subject}</option>
                        ))}
                    </select>

                    <label className={styles.label} htmlFor="language-select">Language of Tutoring</label>
                    <select className={styles.select} id="language-select" name="language" onChange={handleLanguageChange} value={language}>
                        <option value="">Select Language</option>
                        <option value="English">English</option>
                        <option value="Chinese">Chinese</option>
                        <option value="Spanish">Spanish</option>
                        <option value="Hindi">Hindi</option>
                        <option value="Arabic">Arabic</option>
                        <option value="Bengali">Bengali</option>
                        <option value="Portuguese">Portuguese</option>
                        <option value="Russian">Russian</option>
                        <option value="Japanese">Japanese</option>
                        <option value="German">German</option>
                        <option value="French">French</option>
                        <option value="Others">Others</option>
                    </select>

                    <label className={styles.label} htmlFor="salary-range">Hourly Salary $10 - $200</label>
                    <input className={styles.input} type="range" id="salary-range" name="Salary" min="10" max="200" />
                    <input className={styles.input} type="submit" value="Search" />
                </form>
            </div>
        </div>
    );
};

export default StudentSearchBox;
