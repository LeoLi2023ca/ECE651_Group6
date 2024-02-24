"use client"

import styles from "./refer-a-friend.module.css"
import { useState } from 'react';

const ReferAFriendPage = () => {
    const [referralCode] = useState('ABCabc123');

    const handleCopyCode = () => {
        navigator.clipboard.writeText(referralCode).then(() => {
            alert('Referral code copied to clipboard!');
        }).catch(err => {
            console.error('Could not copy text: ', err);
        });
    };

    return (
        <div className={styles.container}>

            <main className={styles.main}>
                <h1 className={styles.title}>
                    Learning together is better!
                </h1>

                <div className={styles.referralBox}>
                    <p className={styles.description}>
                        Earn rewards by referring friends to our service! After they purchase $50 you'll get $10 and they'll get $5!
                    </p>
                    <div className={styles.referralCode}>
                        <span>{referralCode}</span>
                        <button onClick={handleCopyCode}>Copy Referral Code</button>
                    </div>
                </div>

                <div className={styles.referralBox}>
                    <p className={styles.description}>
                        To earn rewards, remind your friend to enter "Fill in referral code", select "Refer code", and enter the referral code within 24 hours of registration.
                    </p>
                    <div className={styles.referralCode}>
                        <label >Fill in Referral Code</label>
                        <input />
                    </div>
                </div>
            </main >
        </div >
    )
}


export default ReferAFriendPage;
