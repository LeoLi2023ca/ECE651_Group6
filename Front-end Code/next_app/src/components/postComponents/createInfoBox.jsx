import React from 'react';
import styles from './createInfoBox.module.css';

const CreateInfoBox = ({ post, handleChange }) => {

    const handleSubmit = (e) => {
        e.preventDefault();
        // The form has been submitted. Data processing should be realized by the parent component
    };

    return (
        <form className={styles.infoBox} onSubmit={handleSubmit}>
            <label className={styles.label}>
                Title
                <input
                    className={styles.title}
                    value={post?.title|| ''}
                    onChange={handleChange}
                    name="title"
                />
            </label>
            <label className={styles.label}>
                Date
                <input
                    className={styles.date}
                    value={post?.date || ''}
                    onChange={handleChange}
                    name="date"
                />
            </label>
            <label className={styles.label}>
                Available Time
                <input
                    className={styles.availableTime}
                    value={post?.available_time|| ''}
                    onChange={handleChange}
                    name="available_time"
                />
            </label>
            <div className={styles.flexRow}>
                <label className={styles.label}>
                    Subject
                    <input
                        className={styles.subject}
                        value={post?.subject|| ''}
                        onChange={handleChange}
                        name="subject"
                    />
                </label>
                <label className={styles.label}>
                    Salary
                    <input
                        className={styles.salary}
                        value={post?.salary|| ''}
                        onChange={handleChange}
                        name="salary"
                    />
                </label>
            </div>
            <label className={styles.label}>
                Info
                <textarea
                    className={styles.msg}
                    value={post?.msg|| ''}
                    onChange={handleChange}
                    name="msg"
                />
            </label>
            <button type="submit">Save</button>
        </form>
    );
};

export default CreateInfoBox;
