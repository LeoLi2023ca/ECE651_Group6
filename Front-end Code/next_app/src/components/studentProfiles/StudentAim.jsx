"use client"
import { useState } from 'react';
import styles from './StudentAim.module.css';

const StudentAim = ({ resumeText }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleToggle = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div>
            <div>
                <h1>Aim</h1>
            </div>
            <div className={styles.container}>
                <p className={isExpanded ? styles.expanded : styles.collapsed}>{resumeText}</p>
                <button onClick={handleToggle} className={styles.button}>
                    {isExpanded ? 'Read Less' : 'Read More'}
                </button>
            </div>
        </div>

    );
};

export default StudentAim;