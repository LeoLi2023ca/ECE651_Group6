import React, { useState } from "react";
import Head from "next/head";
import styles from "./tutorSearchBox.module.css";

const TutorSearchBox = () => {
    const [degree, setDegree] = useState("");
    const [subjects, setSubjects] = useState("");
    const [language, setLanguage] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Form submitted with degree:', degree, ', subjects:', subjects, ', language:', language);
    };

    const handleDegreeChange = (event) => {
        setDegree(event.target.value);
    };

    const handleSubjectsChange = (event) => {
        setSubjects(event.target.value);
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
                    <label className={styles.label} htmlFor="grade-select">Degree</label>
                    <select className={styles.select} id="grade-select" name="degree" onChange={handleDegreeChange} value={degree}>
                        <option value="">Select Degree</option>
                        <option value="high school">High School</option>
                        <option value="undergraduate program">Undergraduate Program</option>
                        <option value="Master program">Master Program</option>
                        <option value="PhD program">PhD Program</option>
                    </select>

                    <label className={styles.label} htmlFor="subject-select">Subjects</label>
                    <select className={styles.select} id="subject-select" name="subject" onChange={handleSubjectsChange} value={subjects}>
                        <option value="">Select Subjects</option>
                        <option value="Physics">Physics</option>
                        <option value="Chemistry">Chemistry</option>
                        <option value="Biology">Biology</option>
                        <option value="Earth Science">Earth Science</option>
                        <option value="Astronomy">Astronomy</option>
                        <option value="Computer Science">Computer Science</option>
                        <option value="Electrical Engineering">Electrical Engineering</option>
                        <option value="Mechanical Engineering">Mechanical Engineering</option>
                        <option value="Chemical Engineering">Chemical Engineering</option>
                        <option value="Civil Engineering">Civil Engineering</option>
                        <option value="Medicine">Medicine</option>
                        <option value="Nursing">Nursing</option>
                        <option value="Pharmacy">Pharmacy</option>
                        <option value="Public Health">Public Health</option>
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

export default TutorSearchBox;
