
# Movie Ticket Booking System

## Assignment Information

- Course: CSCN73010 - Software Quality III: Build and Release
- Assignment: Assignment 4
- Semester: Fall 2026
- Student: Anagha Mampuzha

## Project Overview

A Python-based Movie Ticket Booking System demonstrating
software packaging, automated acceptance testing, and
Application Driver Layer abstraction.

## Business Rules

1. Customers must be at least 13 years old.
2. Ticket quantity must be greater than zero.
3. Requested tickets cannot exceed available seats.
4. Successful bookings reduce available seats.
5. Sold-out movies cannot accept additional bookings.

## Technologies

- Python 3.12.5
- setuptools
- wheel
- build
- pytest
- Git and GitHub

## Development Environment Setup

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install build pytest
    python -m pip install -e .

## Build Distribution Packages

    python -m build

Generated artifacts in the dist directory:

- movie_booking_system-1.0.0.tar.gz
- movie_booking_system-1.0.0-py3-none-any.whl

## Install in a Clean Environment

From the project root in PowerShell:

    $wheel = (Resolve-Path .\dist\*.whl).Path
    deactivate
    cd $HOME
    New-Item -ItemType Directory -Force Assignment4_CleanTest
    cd Assignment4_CleanTest
    python -m venv .venv-clean
    .\.venv-clean\Scripts\Activate.ps1
    Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    python -m pip install "$wheel"
    python -m pip show movie-booking-system

## Execute the Application

    python -m movie_booking

Alternatively:

    movie-booking

Expected result: a successful booking of two tickets,
reducing the available seats from 20 to 18.

## Application Driver Layer

The BookingDriver provides an abstraction between
acceptance tests and the underlying business logic.

Acceptance tests interact exclusively with the driver
to create movies, create customers, perform bookings,
and verify booking outcomes and remaining seats.

## Automated Testing

Run the following commands from the project root
using the development environment.

Unit tests:

    python -m pytest tests/unit -v

Acceptance tests:

    python -m pytest tests/acceptance -v

Complete test suite:

    python -m pytest -v

## Acceptance Scenarios

1. Successful booking
2. Minimum eligible age and exact seat availability
3. Underage customer
4. Zero ticket quantity
5. Negative ticket quantity
6. Insufficient available seats
7. Sold-out movie
8. Multiple successful bookings

All acceptance tests follow the Given/When/Then format.

## Test Results

| Test Type | Passed | Failed |
|-----------|--------|--------|
| Unit Tests | 2 | 0 |
| Acceptance Tests | 8 | 0 |
| Total | 10 | 0 |

All five business rules are covered by automated tests.

## Repository

https://github.com/AnuBuilds/Startercode_Assignment4
