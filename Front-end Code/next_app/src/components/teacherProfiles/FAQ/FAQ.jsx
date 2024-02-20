"use client"
// components/FAQ.jsx
import React, { useState } from 'react';
import styles from './FAQ.module.css';

const FAQ = ({ faqList }) => {
    const [activeIndices, setActiveIndices] = useState([]);

    const toggleFAQ = (index) => {
        setActiveIndices(activeIndices.includes(index)
            ? activeIndices.filter(i => i !== index)
            : [...activeIndices, index]);
    };

    return (
        <div>
            <div>
                <h1>Frequently Asked Questions</h1>
            </div>
            <div className={styles.faqContainer}>
                {faqList.map((faq, index) => (
                    <div className={styles.faqItem} key={index}>
                        <button className={styles.faqQuestion} onClick={() => toggleFAQ(index)}>
                            {faq.question}
                        </button>
                        <div
                            className={`${styles.faqAnswer} ${activeIndices.includes(index) ? styles.active : ''}`}
                        >
                            {faq.answer}
                        </div>
                    </div>
                ))}
            </div>
        </div>

    );
};

export default FAQ;
