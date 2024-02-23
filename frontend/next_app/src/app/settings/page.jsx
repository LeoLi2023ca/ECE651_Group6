"use client"

import styles from "./settings.module.css"
import React, { useState } from 'react';

const SettingsPage = () => {
    const [theme, setTheme] = useState('light');
    const [privacySetting, setPrivacySetting] = useState('Public');
    const [contactPermission, setContactPermission] = useState('Public');
    const [showChangePassword, setShowChangePassword] = useState(false);
    const [currentPassword, setCurrentPassword] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmNewPassword, setConfirmNewPassword] = useState('');

    const handleThemeChange = (event) => {
        setTheme(event.target.value);
    };

    const handlePrivacyChange = (event) => {
        setPrivacySetting(event.target.value);
    };

    const handleContactPermissionChange = (event) => {
        setContactPermission(event.target.value);
    };

    const handleShowChangePassword = (event) => {
        setShowChangePassword(event.target.checked);
    };

    const handlePasswordChange = (event) => {
        const { name, value } = event.target;
        if (name === 'currentPassword') setCurrentPassword(value);
        if (name === 'newPassword') setNewPassword(value);
        if (name === 'confirmNewPassword') setConfirmNewPassword(value);
    };

    const handleSubmitPasswordChange = () => {
        if (newPassword !== confirmNewPassword) {
            alert("New passwords don't match!");
            return;
        }
        alert('Password change submitted!');
    };

    return (
        <div className={styles.container}>
            <h1 className={styles.header}>Settings</h1>

            <div className={styles.term}>
                <label className={styles.label}>Theme:</label>
                <select value={theme} onChange={handleThemeChange} className={styles.select}>
                    <option value="light">Light</option>
                    <option value="dark">Dark</option>
                </select>
            </div>

            <div className={styles.term}>
                <label className={styles.label}>Privacy:</label>
                <select value={privacySetting} onChange={handlePrivacyChange} className={styles.select}>
                    <option value="Public">Public</option>
                    <option value="Private">Private</option>
                </select>
            </div>

            <div className={styles.term}>
                <label className={styles.label}>Contact Permissions:</label>
                <select value={contactPermission} onChange={handleContactPermissionChange} className={styles.select}>
                    <option value="Public">Public</option>
                    <option value="Mutual">Mutual</option>
                    <option value="None">None</option>
                </select>
            </div>

            <div className={styles.term}>
                <label className={styles.label}>Change Password</label>
                <input className={styles.checkbox}
                    type="checkbox"
                    onChange={handleShowChangePassword}
                    
                />
            </div>

            {showChangePassword && (
                <>
                    <div className={styles.term}>
                        <label className={styles.label}>Current Password:</label>
                        <input  className={styles.input}
                            type="password"
                            name="currentPassword"
                            value={currentPassword}
                            onChange={handlePasswordChange}
                        />
                    </div>
                    <div className={styles.term}>
                        <label className={styles.label}>New Password:</label>
                        <input   className={styles.input}
                            type="password"
                            name="newPassword"
                            value={newPassword}
                            onChange={handlePasswordChange}
                        />
                    </div>
                    <div className={styles.term}>
                        <label className={styles.label}>Confirm New Password:</label>
                        <input  className={styles.input}
                            type="password"
                            name="confirmNewPassword"
                            value={confirmNewPassword}
                            onChange={handlePasswordChange}
                        />
                    </div>
                    <button onClick={handleSubmitPasswordChange} className={styles.button}>
                        Change Password
                    </button>
                </>
            )}

        </div>
    );
};

export default SettingsPage;
