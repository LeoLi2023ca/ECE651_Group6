"use client"
// components/TutorProfileHeader.jsx
import React from 'react';
import styles from './TutorProfileHeader.module.css';

const TutorProfileHeader = ({ name, avatarUrl, subject, tagline }) => (
    <div className={styles.headerContainer}>
        <img src={avatarUrl} alt={`${name}'s avatar`} className={styles.avatar} />
        <div className={styles.profileInfo}>
            <h1 className={styles.name}>{name}</h1>
            <h2 className={styles.subject}>{subject}</h2>
            <p className={styles.tagline}>{tagline}</p>
        </div>
    </div>
);

export default TutorProfileHeader;
