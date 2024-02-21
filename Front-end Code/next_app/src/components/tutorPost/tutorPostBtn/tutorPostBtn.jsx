"use client"

import TutorCreatePostPage from "../tutorCreatePost/tutorCreatePost";
import TutorHistoryPostPage from "../tutorHistoryPost/tutorHistoryPost";
import TutorMyPostPage from "../tutorMyPost/tutorMyPost";
import styles from "./tutorPostBtn.module.css";
import React, { useState } from 'react';

const TutorPostBtnPage = () => {
    const [activeTab, setActiveTab] = useState('myPost');

    return (
        <div className={styles.container}>
            <div className={styles.sidebar}>
                <button className={styles.button} onClick={() => setActiveTab('myPost')}>My Post</button>
                <button className={styles.button} onClick={() => setActiveTab('historyPost')}>History Post</button>
                <button className={styles.button} onClick={() => setActiveTab('create')}>Create</button>
            </div>
            <div className={styles.contentArea}>
                {activeTab === 'myPost' && <TutorMyPostPage />}
                {activeTab === 'historyPost' && <TutorHistoryPostPage />}
                {activeTab === 'create' && <TutorCreatePostPage />}
            </div>
        </div>
    );
};


export default TutorPostBtnPage;