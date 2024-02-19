"use client";

import styles from "./registerForm.module.css";
import React, { useState } from "react";

const RegisterForm = ({ onFormSwitch }) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(email, password, name);
    };

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Register</h1>
            <form className={styles.registerForm} onSubmit={handleSubmit}>
                <label className={styles.label} htmlFor="name">Username</label>
                <input className={styles.input}
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                    type="text"
                    id="name"
                    name="name"
                />
                <label className={styles.label} htmlFor="email">Email</label>
                <input className={styles.input}
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                    type="email"
                    id="email"
                    name="email"
                />
                <label className={styles.label} htmlFor="password">Password</label>
                <input className={styles.input}
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                    type="password"
                    id="password"
                    name="password"
                />
                <button className={styles.button} type="submit">Register</button>
            </form>
            <button className={styles.link} onClick={() => onFormSwitch("log in")}>Already have an account? Log in.</button>
        </div>
    );
};

export default RegisterForm;

