"use client";

import React, { useState, useEffect } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const TimeSlotTable = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [weekDates, setWeekDates] = useState([]);
  const [selectedSlots, setSelectedSlots] = useState(new Set());
  const hours = Array.from({ length: 12 }, (_, i) => 8 + i);

  // 计算一周的日期
  useEffect(() => {
    const startOfWeek = selectedDate.getDate() - selectedDate.getDay() + (selectedDate.getDay() === 0 ? -6 : 1);
    const dates = Array.from({ length: 7 }, (_, i) => 
      new Date(selectedDate.getFullYear(), selectedDate.getMonth(), startOfWeek + i)
    );
    setWeekDates(dates);
  }, [selectedDate]);

  // 假设的预约数据，实际应从数据库或API获取
  const appointments = {
    // 示例数据结构
  };

  const toggleSlot = (dayIndex, hour) => {
    const date = weekDates[dayIndex];
    const slotKey = `${date.toLocaleDateString()}-${hour}`;
    if (selectedSlots.has(slotKey)) {
      selectedSlots.delete(slotKey);
    } else {
      selectedSlots.add(slotKey);
    }
    setSelectedSlots(new Set(selectedSlots));
  };

  const isBooked = (dayIndex, hour) => {
    // 需要根据实际的数据结构来判断是否已预约
  };

  const isSelected = (dayIndex, hour) => {
    const date = weekDates[dayIndex];
    return selectedSlots.has(`${date.toLocaleDateString()}-${hour}`);
  };

  const handleSubmit = () => {
    // 处理提交逻辑
    console.log('Selected slots:', Array.from(selectedSlots));
  };

  return (
    <div>
      <DatePicker selected={selectedDate} onChange={date => setSelectedDate(date)} />
      <table>
        <thead>
          <tr>
            <th>Time</th>
            {weekDates.map(date => (
              <th key={date}>
                {date.toLocaleDateString()} ({date.toLocaleString('default', { weekday: 'short' })})
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {hours.map(hour => (
            <tr key={hour}>
              <td>{`${hour}:00`}</td>
              {weekDates.map((date, dayIndex) => (
                <td
                  key={date}
                  style={{ backgroundColor: isBooked(dayIndex, hour) ? 'red' : isSelected(dayIndex, hour) ? 'blue' : 'green' }}
                  onClick={() => !isBooked(dayIndex, hour) && toggleSlot(dayIndex, hour)}
                >
                  {isBooked(dayIndex, hour) ? 'Booked' : isSelected(dayIndex, hour) ? 'Selected' : 'Available'}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={handleSubmit}>Submit Selection</button>
    </div>
  );
};

export default TimeSlotTable;
