import styles from "./loginForm.module.css";
import { useState } from "react";
import axios from "axios";

const LoginForm = ({ onFormSwitch }) => {
    const [email, setEmail] = useState("");
    const [pass, setPass] = useState("");
    const [loading, setLoading] = useState(false); // Added loading state
    const [error, setError] = useState(""); // Added error state

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true); // Start loading
        setError(""); // Reset error message

        try {
            // Replace 'http://localhost:5000/login' with your actual backend endpoint
            const response = await axios.post('http://127.0.0.1:5000/login', {
                email,
                password: pass, // Ensure your backend is expecting 'password' as the key
            });
            
            // Handle response here
            if(response.status === 200) {
                alert("Login successful!");
                console.log("Login successful");
                // login();
            }
            // console.log(response.data);
            // Redirect user to another page or update the state to indicate successful login
        } catch (error) {
            // Handle error here
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                setError("Login failed: Email or Password is incorrect!"); // Example error handling
            } else if (error.request) {
                // The request was made but no response was received
                console.log(error.request);
                setError("Login failed: No response from the server");
            } else {
                // Something happened in setting up the request that triggered an Error
                console.log('Error', error.message);
                setError("Login failed: Email or password is incorrect!");
            }
        } finally {
            setLoading(false); // Stop loading
        }
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
