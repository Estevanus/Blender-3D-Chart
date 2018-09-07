'''
		This  oscphys script made by G. E. Oscar Toreh
		Version 0.0.0.1
		Tested in python 3.5.1
		
		Source  : https://physics.info
'''

from math import *

getVelocity = lambda deltaRange, deltaTime: deltaRange / deltaTime
#velocity

getAcceleration = lambda deltaVelocity, deltaTime: deltaVelocity / deltaTime
#acceleration

lastVelocity = lambda firstVelocity, acceleration, time: firstVelocity + acceleration*time
#motion

getLastPosition = lambda firstPosition, firstVelocity, time, acceleration: firstPosition + firstVelocity*time + 0.5*acceleration*time**2
#motion2

getVelocityOfMotion = lambda currentVelocity, firstVelocity: 0.5 * (currentVelocity + firstVelocity)
#motion3

getForce = lambda mass, acceleration: mass * acceleration
#newton second law

getForce2 = lambda momentum, time: momentum / time

getWeight = lambda mass, gravity: mass * gravity
#weight

getKineticFriction = lambda frictionCoefficient, watt: frictionCoefficient * watt
#dry friction

getCentriAccel = lambda velocity, radius: velocity**2 / radius
#centripetal accel
getCentriAccel2 = lambda w, radius: -w**2*radius
#centripetal accel

getMomentum = lambda mass, velocity: mass * velocity
#momentum

J = lambda force, deltaTime: force*deltaTime
#impulse

Fm = lambda deltaTime, mass, deltaVelocity: mass * deltaVelocity / deltaTime
#impulse-momentum
getImpulseOfMomentum = lambda mass, deltaVelocity: mass * deltaVelocity
#impulse-momentum

getWatt = lambda force, deltaPos, degree: force * deltaPos * cos(radians(degree))
#work

getDeltaEnergy = lambda force, deltaPos, degree: force * deltaPos * cos(radians(degree))
#work-engergy

getKinetic = lambda mass, velocity: 0.5 * mass * velocity**2
#kinetic energy
getKinetic2 = lambda power, mass: power**2 / mass
#kinetic energy

#general p.e. will be available soon

getGravitationalPotentialEnergy = lambda mass, gravity, deltaDistance: mass * gravity * deltaDistance
#gravitational p.e.

getEfficiency = lambda wattOut, energyIn: wattOut / energyIn
#efficiency

getPower = lambda deltaWatt, deltaTime: deltaWatt / deltaTime
#power

getPowerVel = lambda force, velocity, degree: force * velocity * cos(radians(degree))
#power-velocity
getPowerVel2 = lambda force, velocity: force * velocity
#power-velocity

getAngularVel = lambda deltaDegree, deltaTime: deltaDegree / deltaTime
#angular velocity
getAngularVel2 = lambda angularVel, radius: angularVel
#angular velocity

getAngularAcc = lambda deltaAngularVel, deltaTime: deltaAngularVel / deltaTime
#angular acceleration
getAngularAcc2 = lambda angularAcc, radius, angularVel: angularAcc * radius - angularVel**2 * radius
#angular acceleration

getAngularVelOfRot = lambda firstAngularVel, angularAcc, time: firstAngularVel + angularAcc * time
#equation of rotation
getRad = lambda firstRad, firstAngularVel, time, angularAcc: firstRad + firstAngularVel*time + 0.5*angularAcc*time**2 #rad os radians
#equation of rotation
getAngularVelOfRot2 = lambda currentAngularVel, firstAngularVel: 0.5 * (currentAngularVel + firstAngularVel)
#equation of rotation

getTorque = lambda rF, degree: rF * sin(radians(degree))
#torque
getTorque2 = lambda radius, force: radius * force
#torque

#second law of rotation will be available soon


#moment of inertia will be available soon

getWattOfRot = lambda torque, deltaRad: torque * deltaRad
#rotational work


getRotPower = lambda torque, angularVel, rad: torque * angularVel * cos(rad)
#rotational power
getRotPower2 = lambda torque, angularVel: torque * angularVel
#rotational power

getKineticOfRot = lambda inertia, angularVel: 0.5 * inertia * angularVel**2
#rotational kinematic energi nanti menyusul

getAngularMomentum = lambda mass, radius, velocity, rad: mass * radius * velocity * sin(rad)
#angular momentum
getAngularMomentum2 = lambda radius, momentum: radius * momentum
#angular momentum
getAngularMomentum3 = lambda inertia, angularVel: inertia * angularVel
#angular momentum


getAngularImpulse = lambda torque, deltaTime: torque * deltaTime
#angular impulse

getAngularImpulseOfMomentum = lambda mass, deltaAngularVel: mass * deltaAngularVel
#angular impulse momentum

#universal gravitation will be available soon

#gravitional field will be available soon

UGravity = lambda gravity, mass1, mass2, radius: -(gravity * mass1 * mass2 / radius)
#gravitational potential energy
VGravity = lambda gravity, mass, radius: -(gravity * mass / radius)
#gravitational potential energy

getOrbitalSpeed = lambda gravity, mass, radius: sqrt(gravity*mass / radius)
#orbital speed

getEscapeSpeed = lambda gravity, mass, radius: sqrt(2*gravity*mass / radius)
#escape speed

hF = lambda k, delta_x: k * delta_x
#hookie's law

getSpringPotentialEnergy = lambda k, delta_x: 0.5*k*delta_x**2
#spring potential energy

getT = lambda mass, k: 2 * pi * sqrt(mass/k)
#simple harmonic ocillator

#simple pendulum will be available soon

getFreq = lambda T: 1/T
#frequency

getAngularFreq = lambda freq: 2 * pi * freq
#angular frequency

getDensity = lambda mass, volume: mass / volume
#density

getPressure = lambda F, frontalArea: F/frontalArea
#pressure

getPressureInFluid = lambda firstPressure, density, g, h: firstPressure + density * g * h
#pressure in fluid

getBuoyancy = lambda density, g, displacedVolume: density * g * displacedVolume
#buoyancy

getMassFlowRate = lambda deltaMass, deltaTime: deltaMass / deltaTime
#mass flow rate

getVolumeFlowRate = lambda deltaVolume, deltaTime: deltaVolume / deltaTime
#volume flow rate

#dynamic viscosity might avaiable later

getKinematicViscosity = lambda n, density: n / density
#kinematic viscosity

getDragForce = lambda velocity, frontalArea, fluidDensity, dragCoefficient:	0.5 * fluidDensity * velocity**2 * dragCoefficient * frontalArea
#drag

getMach = lambda velocity, c: velocity / c
#mac number

getReynolds = lambda density, velocity, D, n: density * velocity * D / n
#reynolds number

#froude number will be available soon


#young's modulus might be available later

#shear modulus might be available later

#bulk modulus might be available later

#surface tension will be available soon

getMaxSpeed = lambda force, frontalArea, fluidDensity, dragCoefficient:	sqrt(force / frontalArea / dragCoefficient / fluidDensity / 0.5)
#get max speed from drag factor

