"use client"
import { useState } from 'react';
import styles from './TutorIntroduction.module.css';

const TutorIntroduction = ({ introText }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleToggle = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div>
            <div>
                <h1>Introduction</h1>
            </div>
            <div className={styles.container}>
                <p className={isExpanded ? styles.expanded : styles.collapsed}>{introText}</p>
                <button onClick={handleToggle} className={styles.button}>
                    {isExpanded ? 'Read Less' : 'Read More'}
                </button>
            </div>
        </div>
    );
};

export default TutorIntroduction;