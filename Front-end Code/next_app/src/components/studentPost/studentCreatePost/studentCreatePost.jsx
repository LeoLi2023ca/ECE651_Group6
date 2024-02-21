import styles from "./studentCreatePost.module.css"
import CreatePost from "@/components/postComponents/createPost";


const StudentCreatePostPage = () => {
    return (
        <div className={styles.container}>
            <CreatePost/>
        </div>
    )

};

export default StudentCreatePostPage;