import React, { useState } from 'react';
import styles from './editInfoBox.module.css';

const EditInfoBox = ({ post }) => {
    // initialization state
    const [formData, setFormData] = useState({
        title: post.title,
        date: post.date,
        available_time: post.available_time,
        subject: post.subject,
        salary: post.salary,
        msg: post.msg,
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevFormData => ({
            ...prevFormData,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Update the database here

        console.log(formData);
    };

    return (
        <form className={styles.infoBox} onSubmit={handleSubmit}>
            <label className={styles.label}>
                Title
                <input
                    className={styles.title}
                    value={formData.title}
                    onChange={handleChange}
                    name="title"
                />
            </label>
            <label className={styles.label}>
                Date
                <input
                    className={styles.date}
                    value={formData.date}
                    onChange={handleChange}
                    name="date"
                />
            </label>
            <label className={styles.label}>
                Available Time
                <input
                    className={styles.availableTime}
                    value={formData.available_time}
                    onChange={handleChange}
                    name="available_time"
                />
            </label>
            <div className={styles.flexRow}>
                <label className={styles.label}>
                    Subject
                    <input
                        className={styles.subject}
                        value={formData.subject}
                        onChange={handleChange}
                        name="subject"
                    />
                </label>
                <label className={styles.label}>
                    Salary
                    <input
                        className={styles.salary}
                        value={formData.salary}
                        onChange={handleChange}
                        name="salary"
                    />
                </label>
            </div>
            <label className={styles.label}>
                Message
                <textarea
                    className={styles.msg}
                    value={formData.msg}
                    onChange={handleChange}
                    name="msg"
                />
            </label>
            <button type="submit">Save</button>
        </form>
    );
};

export default EditInfoBox;
