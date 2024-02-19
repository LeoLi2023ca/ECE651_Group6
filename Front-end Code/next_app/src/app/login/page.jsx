"use client";

import React, { useState } from "react";
import styles from "./login.module.css"
import LoginForm from "@/components/loginForm/loginForm";
import RegisterForm  from "@/components/registerForm/registerForm";

const LoginRegisterPage = () => {
    const [currentForm, setCurrentForm] = useState("log in");

    const toggleForm = (formName) => {
        setCurrentForm(formName);
    };

    return (
        <div className={styles.container}>
            {currentForm === "log in" ? (
                <LoginForm onFormSwitch={toggleForm} />
            ) : (
                <RegisterForm onFormSwitch={toggleForm} />
            )}
        </div>
    );
};

export default LoginRegisterPage;
