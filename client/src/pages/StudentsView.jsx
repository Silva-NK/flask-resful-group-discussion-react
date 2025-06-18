import React, { useState, useEffect } from 'react'
import { Routes, Route } from 'react-router-dom';

// import './App.css'

function StudentsView() {
    const [students, setStudents] = useState([])

    useEffect(() => {
        fetch('http://localhost:5555/students')
        .then((response) => response.json())
        .then((data) => setStudents(data))
        .catch((err) => console.error("Error fetching students: ", err))
    }, []);

  return (
    <>
      <div classname = 'container'>
        <h2>Student List</h2>
        <table classname="table">
          <thead>
            <tr>
              <th>Serial No.</th>
              <th>Student Name</th>
            </tr>
          </thead>
          <tbody>
            {students.length > 0 ? (
              students.map((student, index) => (
              <tr key={student.id}>
                <td data-label="ID">{index +1}</td>
                <td data-label="Name">{student.name}</td>
              </tr>
              ))     
            ) : (
              <tr>
                  <td colSpan="2" style={{ textAlign: "center", fontStyle: "italic" }}>
                      No students found.
                  </td>
              </tr>
                    )}
          </tbody>
        </table>
      </div>
    </>
  )
}

export default StudentsView
