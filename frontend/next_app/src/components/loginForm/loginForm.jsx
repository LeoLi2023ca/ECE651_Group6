import styles from "./loginForm.module.css";
import { useState } from "react";
import axios from "axios";

const LoginForm = ({ onFormSwitch }) => {
    const [email, setEmail] = useState("");
    const [pass, setPass] = useState("");
    localStorage.setItem('isTutor', false);

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log(email);
        localStorage.setItem('isTutor', true);

        // Login with back-end code
    };

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Log in</h1>
            {error && <div className={styles.error}>{error}</div>} {/* Display error message */}
            <form className={styles.loginForm} onSubmit={handleSubmit}>
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
                    value={pass}
                    onChange={(event) => setPass(event.target.value)}
                    type="password"
                    id="password"
                    name="password"
                />
                <button className={styles.button} type="submit" disabled={loading}>
                    {loading ? 'Logging in...' : 'Log in'}
                </button>
            </form>
            <button className={styles.link} onClick={() => onFormSwitch("register")}>Don't have an account? Register now.</button>
        </div>
    );
};

export default LoginForm;
