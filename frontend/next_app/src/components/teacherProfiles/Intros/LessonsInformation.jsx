"use client"
// components/LessonsInformation.jsx
import { useState } from 'react';
import styles from './LessonsInformation.module.css';

const LessonsInformation = ({ lessonInfo }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleToggle = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div>
            <div>
                <h1>Lessions Information</h1>
            </div>
            <div className={styles.container}>
                <p className={isExpanded ? styles.expanded : styles.collapsed}>{lessonInfo}</p>
                <button onClick={handleToggle} className={styles.button}>
                    {isExpanded ? 'Show Less' : 'Show More'}
                </button>
            </div>
        </div>
    );
};

export default LessonsInformation;
