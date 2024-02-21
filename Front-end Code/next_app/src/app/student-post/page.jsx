import styles from "./student-post.module.css"
import StudentPost from "@/components/studentPost/studentPost";

const StudentPostPage = () => {
    return (
        <div className={styles.container}>
            <StudentPost/>
        </div>
    )
};

export default StudentPostPage;