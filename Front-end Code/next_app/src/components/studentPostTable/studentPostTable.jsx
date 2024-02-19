import styles from "./studentPostTable.module.css"


const StudentPostTable = ({ data }) => { 

    return (
        <div className={styles.container}>
            <table className={styles.postTable}>
                <thead>
                    <tr>
                        <th className={styles.tableHeader}>Username</th>
                        <th className={styles.tableHeader}>Gender</th>
                        <th className={styles.tableHeader}>School</th>
                        <th className={styles.tableHeader}>Grade</th>
                        <th className={styles.tableHeader}>Subjects</th>
                        <th className={styles.tableHeader}>Language</th>
                        <th className={styles.tableHeader}>Schedule</th>
                        <th className={styles.tableHeader}>Timezone</th>
                        <th className={styles.tableHeader}>Salary</th>
                        <th className={styles.tableHeader}>Date</th>
                    </tr>
                </thead>
                <tbody>
                {data.map((post) => ( 
                    <tr key={post.id}>
                        <td className={styles.tableCell}>{post.Username}</td>
                        <td className={styles.tableCell}>{post.Gender}</td>
                        <td className={styles.tableCell}>{post.School}</td>
                        <td className={styles.tableCell}>{post.Grade}</td>
                        <td className={styles.tableCell}>{post.Subjects}</td>
                        <td className={styles.tableCell}>{post.Language}</td>
                        <td className={styles.tableCell}>{post.Schedule}</td>
                        <td className={styles.tableCell}>{post.Timezone}</td>
                        <td className={styles.tableCell}>{post.Salary}</td>
                        <td className={styles.tableCell}>{post.Date}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
};

export default StudentPostTable;
