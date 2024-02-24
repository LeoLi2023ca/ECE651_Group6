"use client"

import StudentCreatePostPage from "../studentCreatePost/studentCreatePost";
import StudentHistoryPostPage from "../studentHistoryPost/studentHistoryPost";
import StudentMyPostPage from "../studentMyPost/studentMyPost";
import styles from "./studentPostBtn.module.css";
import React, { useState } from 'react';

const StudentPostBtnPage = () => {
    const [activeTab, setActiveTab] = useState('myPost');

    return (
        <div className={styles.container}>
            <div className={styles.sidebar}>
                <button className={styles.button} onClick={() => setActiveTab('myPost')}>My Post</button>
                <button className={styles.button} onClick={() => setActiveTab('historyPost')}>History Post</button>
                <button className={styles.button} onClick={() => setActiveTab('create')}>Create</button>
            </div>
            <div className={styles.contentArea}>
                {activeTab === 'myPost' && <StudentMyPostPage />}
                {activeTab === 'historyPost' && <StudentHistoryPostPage />}
                {activeTab === 'create' && <StudentCreatePostPage />}
            </div>
        </div>
    );
};


export default StudentPostBtnPage;