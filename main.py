from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
appointments = []
next_appointment_id = 1


class Appointment(BaseModel):
    patient_name: str
    doctor_id: int
    date: str
    time: str


@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    for i in appointments:
        if i["id"] == appointment_id:
            return i
    raise HTTPException(
        status_code=404,
        detail="Appointment not found"
    )


@app.post("/appointments")
def create_appointment(appointment: Appointment):
    global next_appointment_id

    new_appointment = {
        "id": next_appointment_id,
        "patient_name": appointment.patient_name,
        "doctor_id": appointment.doctor_id,
        "date": appointment.date,
        "time": appointment.time


    }

    appointments.append(new_appointment)

    next_appointment_id += 1

    return {
        "message": "Appointment created successfully!",
        "appointment": new_appointment
    }


@app.get("/appointments")
def get_appointments():
    return appointments
