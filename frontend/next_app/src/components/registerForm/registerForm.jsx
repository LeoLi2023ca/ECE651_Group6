import styles from "./registerForm.module.css";
import React, { useState } from "react";
import axios from "axios"; // Import Axios

const RegisterForm = ({ onFormSwitch }) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");
    const [loading, setLoading] = useState(false); // State to manage loading
    const [error, setError] = useState(""); // State to manage error messages
    const [id, setId] = useState("Student"); // State to manage user type [Student, Teacher, Admin

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true); // Start loading
        setError(""); // Reset error message

        try {
            // Replace 'http://localhost:5000/register' with your actual backend endpoint
            const response = await axios.post('http://127.0.0.1:5000/register', {
                username: name,
                email,
                password,
                id
            });

            // Handle response here
            console.log(response.data);
            // Example: Clear form fields after successful registration
            setEmail("");
            setPassword("");
            setName("");
            // Optionally, redirect the user or give a success message
        } catch (error) {
            // Handle error here
            if (error.response) {
                // The server responded with a status code outside the 2xx range
                console.log(error.response.data);
                setError("Registration failed: " + error.response.data.message); // Example error handling
            } else if (error.request) {
                // The request was made but no response was received
                console.log(error.request);
                setError("Registration failed: No response from the server");
            } else {
                // Something else caused the request to fail
                console.log('Error', error.message);
                setError("Registration failed: " + error.message);
            }
        } finally {
            setLoading(false); // Stop loading
        }
    };

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Register</h1>
            {error && <div className={styles.error}>{error}</div>} {/* Display error message */}
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
                <div>
                    <label>
                        <input
                            type="radio"
                            value="Student"
                            checked={id === "Student"}
                            onChange={(e) => setId(e.target.value)}
                        />
                        Student
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="Tutor"
                            checked={id === "Tutor"}
                            onChange={(e) => setId(e.target.value)}
                        />
                        Tutor
                    </label>
                </div>
                <button className={styles.button} type="submit" disabled={loading}>
                    {loading ? 'Registering...' : 'Register'}
                </button>
            </form>
            <button className={styles.link} onClick={() => onFormSwitch("log in")}>Already have an account? Log in.</button>
        </div>
    );
};

export default RegisterForm;
