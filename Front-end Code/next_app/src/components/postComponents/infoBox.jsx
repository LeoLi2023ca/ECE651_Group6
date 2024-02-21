import React from 'react';
import styles from './InfoBox.module.css';

const InfoBox = ({ post }) => {
    return (
        <div className={styles.infoBox}>
            <div className={styles.title}>{post.title}</div>
            <div className={styles.date}>Date: {post.date}</div>
            <div className={styles.availableTime}>Available Time: {post.available_time}</div>
            <div className={styles.flexRow}>
                <div className={styles.subject}>Subject: {post.subject}</div>
                <div className={styles.salary}>Salary: {post.salary}</div>
            </div>
            <div className={styles.msg}>{post.msg}</div>
        </div>
    );
};

export default InfoBox;
